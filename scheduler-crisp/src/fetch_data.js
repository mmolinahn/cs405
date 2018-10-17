const Http = new XMLHttpRequest();
const url='http://13.59.120.155:5000/';
Http.open("GET", url);
Http.send();
Http.onreadystatechange=(e)=>{
	console.log(Http.responseText)
}
