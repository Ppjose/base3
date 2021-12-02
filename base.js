//Algoritmo DocIRS

//var sNumero = document.getElementById("numero2").value;
const alfa=[]
const asci=[]
function Decimal_Binario(sNumero,base)
{
var base;
var sTope;
var sTopeMax;
var sCoeficiente=new Array() ;
var sResiduo=-1;
var mm=0;
while (sResiduo!=0)
{
       for(var i=0;i<=100;i++)
      {
              if(Math.pow(base, i)>sNumero)
               {
                 sTope=i-1;
                sResiduo=sNumero-Math.pow(base, sTope);
                break;
               }
       }

if(mm==0){sTopeMax=sTope}
sCoeficiente[sTope]=1
 for(var j=0;j<sTope;j++)
 {
   sCoeficiente[j]=0
 }
    if (sResiduo==0){break}
    sNumero=sResiduo
    mm=mm+1
} 
 numBin=""
  for(var j=0;j<=sTopeMax;j++)
 {
   numBin=numBin + sCoeficiente[j]
  }
 return numBin.split("").reverse().join("");
}
//alert ("El resultado es : " + resultado);
console.log(Decimal_Binario(3450066,150000))
