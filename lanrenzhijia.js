function SetObjNum(n) {
    var a = "";
    for (var i = 0; i < n; i++)
        a += Math.floor(Math.random() * 10);
    return a
}

function nscaler(a) {
    var b = "";
    // $.each(a, function(i, e) {
    for (let i = 0; i < a.length; i++) {
        switch (a[i]) {
            case "0":
                b += "0";
                break;
            case "1":
                b += "2";
                break;
            case "2":
                b += "5";
                break;
            case "3":
                b += "8";
                break;
            case "4":
                b += "6";
                break;
            case "5":
                b += "1";
                break;
            case "6":
                b += "3";
                break;
            case "7":
                b += "4";
                break;
            case "8":
                b += "9";
                break;
            case "9":
                b += "7";
                break
        }
    }
    return b
}


function recode(a, b) {
    var n = nscaler(a);
    var c = SetObjNum(a.length);
    var d = SetObjNum(a.length);
    n = parseInt(n) + parseInt(d);
    // var b = $("#iptstamp").val();
    b = nscaler(b.toString());
    return c + "-" + n + "-" + d + "-" + b
}

function reurl(a, b) {
    let a_href = "/item/" + recode(a.id, b);
    return a_href;
}

var ret = reurl({"id": '3362'}, 1704894044656);
console.log(ret);