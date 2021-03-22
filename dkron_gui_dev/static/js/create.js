var down = document.getElementById("counters");

function createjs() {
    var year = document.createElement("INPUT");
    year.id = "year";
    year.style.display = "none"
    year.setAttribute("type", "number");
    year.setAttribute("placeholder", "Year");
    document.body.appendChild(year);
    var month = document.createElement("INPUT");
    month.id = "month";
    month.style.display = "none"
    month.setAttribute("type", "number");
    month.setAttribute("placeholder", "month");
    document.body.appendChild(month);
    var week = document.createElement("INPUT");
    week.id = "week";
    week.style.display = "none"
    week.setAttribute("type", "number");
    week.setAttribute("placeholder", "week");
    document.body.appendChild(week);
    var day = document.createElement("INPUT");
    day.id = "day";
    day.style.display = "none"
    day.setAttribute("type", "number");
    day.setAttribute("placeholder", "day");
    document.body.appendChild(day);
    var hour = document.createElement("INPUT");
    hour.id = "hour";
    hour.style.display = "none"
    hour.setAttribute("type", "number");
    hour.setAttribute("placeholder", "hour");
    document.body.appendChild(hour);
    var minute = document.createElement("INPUT");
    minute.id = "minute";
    // minute.style.display = "none"
    minute.setAttribute("type", "number");
    minute.setAttribute("placeholder", "minute");
    document.body.appendChild(minute);
}

function opt() {
    year.style.display = "block"
    month.style.display = "block"
    week.style.display = "block"
    day.style.display = "block"
    hour.style.display = "block"
    minute.style.display = "block"
}

function optremove() {
    year.style.display = "none"
    month.style.display = "none"
    week.style.display = "none"
    day.style.display = "none"
    hour.style.display = "none"
    minute.style.display = "none"
}