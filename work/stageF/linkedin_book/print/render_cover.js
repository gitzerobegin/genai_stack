const {chromium}=require('playwright');const path=require('path');(async()=>{const b=await chromium.launch();
const [wrap,out,front,jpg,W,H]=process.argv.slice(2);let p=await b.newPage();await p.goto('file://'+path.resolve(wrap));await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:out,width:W+'in',height:H+'in',printBackground:true,pageRanges:'1'});
p=await b.newPage({viewport:{width:1600,height:2560}});await p.goto('file://'+path.resolve(front));await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:jpg,type:'jpeg',quality:92});await b.close();})();