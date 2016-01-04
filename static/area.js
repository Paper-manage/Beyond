function Dsy() 
{ 
this.Items = {}; 
} 
Dsy.prototype.add = function(id,iArray) 
{ 
this.Items[id] = iArray; 
} 
Dsy.prototype.Exists = function(id) 
{ 
if(typeof(this.Items[id]) == "undefined") return false; 
return true; 
} 
function change(v){ 
var str="0"; 
for(i=0;i<v;i++){ str+=("_"+(document.getElementById(s[i]).selectedIndex-1));}; 
var ss=document.getElementById(s[v]); 
with(ss){ 
length = 0; 
options[0]=new Option(opt0[v],opt0[v]); 
if(v && document.getElementById(s[v-1]).selectedIndex>0 || !v) 
{ 
if(dsy.Exists(str)){ 
ar = dsy.Items[str]; 
for(i=0;i<ar.length;i++)options[length]=new Option(ar[i],ar[i]); 
if(v)options[1].selected = true; 
} 
} 
if(++v<s.length){change(v);} 
} 
} 
var dsy = new Dsy(); 

dsy.add("0",["理学","工学","文学"]); 

dsy.add("0_0",["数学类","物理学类"]); 
dsy.add("0_0_0",["数学与应用数学","信息与计算科学"]); 
dsy.add("0_0_1",["物理学","应用物理学","核物理"]); 

dsy.add("0_1",["力学类","机械类"]); 
dsy.add("0_1_0",["理论与应用力学","工程力学"]); 
dsy.add("0_1_1",["机械工程","机械设计制造及其自动化","材料成型及控制工程"]); 

dsy.add("0_2",["中国语言文学类","外国语言文学类"]); 
dsy.add("0_2_0",["汉语言文学","汉语言","汉语国际教育"]); 
dsy.add("0_2_1",["英语","俄语"]); 



var s=["grade1","grade2","grade3"]; 
var opt0 = ["基本学科","学科","专业"]; 
function setup() 
{ 
for(i=0;i<s.length-1;i++) 
document.getElementById(s[i]).onchange=new Function("change("+(i+1)+")"); 
change(0); 
} 