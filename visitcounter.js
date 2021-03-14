// function DoCount(readcount) {
//     var a = JSON.parse(readcount);
//     document.getElementById("displaycount").innerHTML = readcount;
//     var y = JSON.stringify({vcount:a.vcount});
//     document.getElementById("displaycount").innerHTML = y;
//     y.vcount = readcount;

// }


const jsonURL = '/counter.json';
fetch(jsonURL)
.then(function (response){
    return response.json();
})
.then(function (jsonreader){
    document.getElementById("displaycount").innerHTML = 'あなたは' + jsonreader.count + '人目の訪問者です。';
})

const reader = new XMLHttpRequest();
reader.open('get','http://0.0.0.0:8888/', true);
reader.responseType = 'text';
reader.send();