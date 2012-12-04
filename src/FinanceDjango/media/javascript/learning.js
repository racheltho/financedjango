
function displayDate(txt)
{
document.getElementById(txt).innerHTML=Date();
}

function welcome(pid)
{
	var name = prompt('Welcome, what is your name?','Type your name here')
	document.getElementById(pid).innerHTML="Hi " + name + ", can you tell me the current time?";
}


function changeImage(image)
{
element=document.getElementById(image)
if (element.src.match("konrad.jpg"))
  {
  element.width = "500";
  element.height = "70";
  element.src="/media/images/wiredQC.gif";
  }
else
  {
  element.width = "350";
  element.height = "200";
  element.src="/media/images/konrad.jpg";
  }
}


function myFunction(box)
{
var x=document.getElementById(box).value;
if(x==""||isNaN(x))
	{
	alert("Not Numeric");
	}
}




