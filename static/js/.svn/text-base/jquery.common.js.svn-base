$.extend({
    format: function() {
        if (arguments.length == 0) {
            return null;
        }
        var str = arguments[0];
        for (var i = 1; i < arguments.length; i++) {
            var re = new RegExp('\\{' + (i - 1) + '\\}', 'gm');
            str = str.replace(re, arguments[i]);
        }
        return str;
    },
    endwith: function(value, str) {
        if (str == null || str == "" || value.length == 0 || str.length > value.length)
            return false;
        if (value.substring(value.length - str.length) == str)
            return true;
        else
            return false;
        return true;
    },
    startwith: function(value, str) {
        if (str == null || str == "" || value.length == 0 || str.length > value.length)
            return false;
        if (value.substring(0, str.length) == str)
            return true;
        else
            return false;
        return true;
    },
    PadLeft: function(value, totalWidth, paddingChar) {
        if (paddingChar != null) {
            return this.PadHelper(value, totalWidth, paddingChar, false);
        } else {
            return this.PadHelper(value, totalWidth, ' ', false);
        }
    },
    PadRight: function(value, totalWidth, paddingChar) {
        if (paddingChar != null) {
            return this.PadHelper(value, totalWidth, paddingChar, true);
        } else {
            return this.PadHelper(value, totalWidth, ' ', true);
        }
    },
    PadHelper: function(value, totalWidth, paddingChar, isRightPadded) {
        if (value.length < totalWidth) {
            var paddingString = new String();
            for (i = 1; i < (totalWidth - value.length); i++) {
                paddingString += paddingChar;
            }
            if (isRightPadded) {
                return (value + paddingString);
            } else {
                return (paddingString + value);
            }
        } else {
            return value;
        }
    },
    parseDate: function(str) {
        var d = new Date(Date.parse(str.replace(/-/g,"/")));   
        return d;
    },
    DateDiff: function(sDate1, sDate2) {
        var aDate, oDate1, oDate2, iDays;
        aDate = sDate1.split("-");
        oDate1 = new Date(aDate[1] + '-' + aDate[2] + '-' + aDate[0]);
        aDate = sDate2.split("-");
        oDate2 = new Date(aDate[1] + '-' + aDate[2] + '-' + aDate[0]);
        iDays = parseInt(Math.abs(oDate1 - oDate2) / 1000 / 60 / 60 / 24);
        return iDays;
    },
    compare:function(oldDate  , newDate) { 
        if(typeof(newDate)!="object" && newDate.constructor != Date){
            return -2; 
        }
        var d = oldDate.getTime() - newDate.getTime();
        if(d>0){
            return 1;
        }else{
            if(d==0){
                return 0;
            }else {
                return -1;
            }
        }
    },
    dateAdd:function( date , interval , number) {
        switch(interval) {
            case "y" : 
            date.setFullYear(date.getFullYear()+number); 
            return date; 
            case "q" : 
            date.setMonth(date.getMonth()+number*3);
            return date; 
            case "m" : 
            date.setMonth(date.getMonth()+number);
            return date; 
            case "w" : 
            date.setDate(date.getDate()+number*7);
            return date; 
            case "d" : 
            date.setDate(date.getDate()+number);
            return date; 
            case "h" : 
            date.setHours(date.getHours()+number);
            return date; 
            case "m" : 
            date.setMinutes(date.getMinutes()+number); 
            return date; 
            case "s" : 
            date.setSeconds(date.getSeconds()+number);
            return date; 
            default : 
            date.setDate(d.getDate()+number);
            return date; 
        }
    },
    formatDate:function(date , formatStr){
        var str = formatStr; 
        str=str.replace(/yyyy|YYYY/,date.getFullYear()); 
        str=str.replace(/yy|YY/,(date.getYear() % 100)>9?(date.getYear() % 100).toString():"0" + (date.getYear() % 100)); 
        str=str.replace(/MM/,date.getMonth()>8?(date.getMonth()+1).toString():"0" + (date.getMonth()+1)); 
        str=str.replace(/M/g,date.getMonth()+1); 
        str=str.replace(/dd|DD/,date.getDate()>9?date.getDate().toString():"0" + date.getDate()); 
        str=str.replace(/d|D/g,date.getDate()); 
        str=str.replace(/hh|HH/,date.getHours()>9?date.getHours().toString():"0" + date.getHours()); 
        str=str.replace(/h|H/g,date.getHours()); 
        str=str.replace(/mm/,date.getMinutes()>9?date.getMinutes().toString():"0" + date.getMinutes()); 
        str=str.replace(/m/g,date.getMinutes()); 
        str=str.replace(/ss|SS/,date.getSeconds()>9?date.getSeconds().toString():"0" + date.getSeconds()); 
        str=str.replace(/s|S/g,date.getSeconds()); 
        return str;
    }
});
jQuery.fn.blindToggle = function(speed, easing, callback) {
  var h = this.height() + parseInt(this.css('paddingTop')) + parseInt(this.css('paddingBottom'));
  return this.animate({marginTop: parseInt(this.css('marginTop')) < 0 ? 0 : -h}, speed, easing, callback);  
};