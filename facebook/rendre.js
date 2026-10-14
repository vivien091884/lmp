// Rend visuel-smtec.png et video-smtec.mp4 pour chaque dossier listé dans dates.json (ou ceux passés en argument).
// Prérequis : npm i playwright-core ; Chromium (CHROMIUM_PATH, défaut /opt/pw-browsers/chromium) ; ffmpeg avec libx264.
const {chromium}=require('playwright-core');const fs=require('fs');const path=require('path');const {execFileSync}=require('child_process');
const FPS=30,DUREE=9.5,T_IMAGE=0;
(async()=>{
 const dirs=process.argv.slice(2).length?process.argv.slice(2):JSON.parse(fs.readFileSync(path.join(__dirname,'dates.json')));
 const b=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:1080,height:1080}});
 const ouvrir=async f=>{await p.goto('file://'+path.resolve(__dirname,f));await p.evaluate(()=>document.fonts.ready);};
 const seek=t=>p.evaluate(ms=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=ms}),t*1000);
 for(const d of dirs){
  const dir=path.resolve(__dirname,d);
  await ouvrir(`${d}/visuel.html`);await p.screenshot({path:`${dir}/visuel-smtec.png`});
  await ouvrir(`${d}/video.html`);
  const tmp=fs.mkdtempSync(path.join(dir,'.img-'));
  for(let i=0;i<Math.round(DUREE*FPS);i++){await seek(i/FPS);await p.screenshot({path:`${tmp}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
  execFileSync('ffmpeg',['-y','-loglevel','error','-framerate',String(FPS),'-i',`${tmp}/f%04d.jpg`,'-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium','-movflags','+faststart',`${dir}/video-smtec.mp4`]);
  fs.rmSync(tmp,{recursive:true});console.log('ok',d);
 }
 await b.close();
})();
