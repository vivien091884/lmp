// Rend les vidéos verticales reel-*.mp4 (1080×1920, 8 s) à partir des reel-*.html de chaque dossier (dossiers en argument, sinon tous).
// Option --apercu : seulement 3 images PNG par vidéo dans .apercu/ pour contrôle.  Prérequis : voir rendre.js.
const {chromium}=require('playwright-core');const fs=require('fs');const path=require('path');const {execFileSync}=require('child_process');
const FPS=30,DUREE=8,PARALLELE=4;
const args=process.argv.slice(2),apercu=args.includes('--apercu');
const dirs=args.filter(a=>!a.startsWith('--'));
const liste=(dirs.length?dirs:fs.readdirSync(__dirname).filter(d=>/^\d{4}-\d\d-\d\d$/.test(d)))
 .flatMap(d=>fs.readdirSync(path.join(__dirname,d)).filter(f=>/^reel-.*\.html$/.test(f)).map(f=>[d,f]));
(async()=>{
 const b=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/opt/pw-browsers/chromium'});
 const travail=async p=>{
  for(let job;(job=liste.shift());){
   const [d,f]=job,dir=path.resolve(__dirname,d),nom=f.replace('.html','');
   await p.goto('file://'+path.join(dir,f));await p.evaluate(()=>document.fonts.ready);
   const seek=t=>p.evaluate(ms=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=ms}),t*1000);
   if(apercu){const out=path.join(__dirname,'.apercu');fs.mkdirSync(out,{recursive:true});
    for(const t of [1.2,4.8,7.6]){await seek(t);await p.screenshot({path:`${out}/${d}_${nom}_${t}.png`});}continue;}
   const tmp=fs.mkdtempSync(path.join(dir,'.img-'));
   for(let i=0;i<DUREE*FPS;i++){await seek(i/FPS);await p.screenshot({path:`${tmp}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});}
   execFileSync('ffmpeg',['-y','-loglevel','error','-framerate',String(FPS),'-i',`${tmp}/f%04d.jpg`,'-c:v','libx264','-pix_fmt','yuv420p','-crf','21','-preset','medium','-movflags','+faststart',`${dir}/${nom}.mp4`]);
   fs.rmSync(tmp,{recursive:true});console.log('ok',d,nom);
  }};
 await Promise.all(Array.from({length:PARALLELE},async()=>travail(await b.newPage({viewport:{width:1080,height:1920}}))));
 await b.close();
})();
