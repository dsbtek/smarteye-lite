class UtilityClass {
  static isObjectLike(obj) {
    return typeof obj === "object" && obj !== null;
  }

  static inArray(arr, elem) {
    if (arr == null || !UtilityClass.isArrayLike(arr))
      throw "{arr} is not an Array";

    if (arr.indexOf(elem) === -1) return false;

    return true;
  }

  static generateCSV(heads, item) {
  
    let header = "",
      headerArray = [],
      bodyArray = [];

    var csv = "";

    heads.forEach(function (row) {
      headerArray.push(row.key);
    });

    header = headerArray.join(",") + "\n";

    item.forEach(function (row) {
      let rowArray = [];
      headerArray.forEach(function (HeadRow) {
        rowArray.push('"' + row[HeadRow] + '"');
      });

      bodyArray.push(rowArray);
    });

    bodyArray.forEach(function (eachItem) {
      header += eachItem.join(",");
      header += "\n";
    });

    csv = "data:text/csv;charset=utf-8," + encodeURI(header);

    return csv;
  }

  static TurnObjectToArray(CollectObject) {
    var FinalArray = [];

    Object.keys(CollectObject).forEach((key) => {
      let value = CollectObject[key];
      FinalArray = [...FinalArray, ...value];
      //use key and value here
    });

    return FinalArray;
  }

  static givemedate(time) {
    var now;
    if (time) {
      now = new Date(time);
    } else {
      now = new Date();
    }

    let day = now.getDate();
    let month = now.getMonth() + 1;
    let year = now.getFullYear();
    let hour = now.getHours();
    let minute = now.getMinutes();
    let second = now.getSeconds();

    return (
      year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second
    );
  }

  static getStationIDS(array) {
    var sitearray = [];
    array.forEach(function (element) {
      sitearray.push(element.Site_id);
    });
    //console.log('station ids',sitearray)
    return sitearray;
  }

  static getCompanyIDS(array) {
    let comapanyarray = [];
    array.forEach(function (element) {
      comapanyarray.push(element.Company);
    });

    return comapanyarray;
  }

  static getTankgroupIDS(array) {
    var tgarray = [];
    array.forEach(function (element) {
      tgarray.push(element.Group_id);
    });
    return tgarray;
  }

  

  //Got this from https://stackoverflow.com/questions/15762768/javascript-math-round-to-two-decimal-places/22977058#answer-15762794
  static RoundUp(n, digits) {
    var negative = false;
    if (digits === undefined) {
      digits = 0;
    }
    if (n < 0) {
      negative = true;
      n = n * -1;
    }
    var multiplicator = Math.pow(10, digits);
    n = parseFloat((n * multiplicator).toFixed(11));
    n = (Math.round(n) / multiplicator).toFixed(digits);
    if (negative) {
      n = (n * -1).toFixed(digits);
    }
    return n;
  }

  static NormalizeDigits(digits) {
    try {
      var parts = digits.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    } catch (error) {console.log(error)}
  }

  static SlashDate(dateString, dateOnly = false) {
    if (dateString) {
      var date = new Date(dateString);

      var year = date.getFullYear();
      var month =
        date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1;
      var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();

      var hour = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
      var minute =
        date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
      // var second =
      //   date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();

      if (dateOnly) {
        return year + "-" + month + "-" + day;
      }

      return year + "-" + month + "-" + day + " " + hour + ":" + minute;
    } else {
      return "";
    }
  }

  static FullTimestamp(dateString) {
    if (dateString) {
      var date = new Date(dateString);

      var year = date.getFullYear();
      var month =
        date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1;
      var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();

      var hour = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
      var minute =
        date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
      var second =
        date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();

      return (
        year +
        "-" +
        month +
        "-" +
        day +
        " " +
        hour +
        ":" +
        minute +
        ":" +
        second
      );
    } else {
      return "";
    }
  }

  static GetISODate(days) {
    var today = new Date();
    if (days) {
      today.setDate(today.getDate() + days);
      return today.toISOString();
    }

    return new Date().toISOString();
  }

  //Note,date2 is usually the bigger date instance
  static DifferencebtwDates(date1, date2) {
    //Get 1 day in milliseconds
    // var one_day = 1000 * 60 * 60 * 24;

    // Convert both dates to milliseconds
    var date1_ms = date1.getTime();
    var date2_ms = date2.getTime();

    // Calculate the difference in milliseconds
    var difference_ms = date2_ms - date1_ms;
    //take out milliseconds
    difference_ms = difference_ms / 1000;

    var seconds = Math.floor(difference_ms % 60);

    difference_ms = difference_ms / 60;
    var minutes = Math.floor(difference_ms % 60);

    difference_ms = difference_ms / 60;
    var hours = Math.floor(difference_ms % 24);
    var days = Math.floor(difference_ms / 24);

    return { days, hours, seconds, minutes };
  }

  static isArrayEmpty(array) {
    if (!array || array === void 0 || array.length == 0) {
      return true;
    }

    return false;
  }

  static RandomString() {
    var randNo =
      Math.floor(Math.random() * 100) +
      2 +
      "" +
      new Date().getTime() +
      Math.floor(Math.random() * 100) +
      2 +
      Math.random()
        .toString(36)
        .replace(/[^a-zA-Z]+/g, "")
        .substr(0, 5);

    return randNo;
  }

  static onSpinner(element) {
    if (!element) return;
    var x = document.querySelectorAll(element);
    var i;
    for (i = 0; i < x.length; i++) {
      x[i].classList.add("cover-roll");
    }

    return true;
  }

  static printRules(styleSheet) {
    const rootEl = document.getElementById("fool");
    const preEl = rootEl.appendChild(document.createElement("pre"));
    preEl.innerHTML = JSON.stringify(
      [...styleSheet.cssRules].map((rule) => rule.cssText),
      null,
      2
    );
  }

  static randomNumber() {
    let r = Math.random().toString(36).substring(8);
    return Date.now() + r;
  }

  static randomStringsOnly(length = 8) {
    var text = "";
    var possible =
      "stuvwxyzRSTUABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzRSTUVWXYZabcdefghijk";

    for (var i = 0; i < length; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
  }

  static Setcss(dom, selector = null, styleString = null) {
    //The selector can be null when its not a styling related to a div or class: Like keyframe
    const sheet = dom.sheet;
    const rule = selector ? `${selector} { ${styleString} }` : `${styleString}`;
    const index = sheet.cssRules.length;

    sheet.insertRule(rule, index);

    return dom;
  }

  static addClass(element, name) {
    var arr, groupnames;
    groupnames = element.className;
    arr = element.className.split(" ");
    if (arr.indexOf(name) == -1) {
      if (groupnames) {
        element.className += " " + name;
      } else {
        element.className = name;
      }
    }

    return element;
  }


  static offSpinner(element) {
    if (!element) return;
    var x = document.querySelectorAll(element);
    var i;
    for (i = 0; i < x.length; i++) {
      x[i].classList.remove("cover-roll");
    }

    return true;
  }

  static stringifyRecordValues(row) {
    /* istanbul ignore else */
    if (row instanceof Object) {
      return (0, UtilityClass.stringifyObjectValues)(row);
    } else {
      /* istanbul ignore next */
      return "";
    }
  }

  static stringifyObjectValues(val) {
    if (typeof val === "undefined" || val === null) {
      /* istanbul ignore next */
      return "";
    }

    if (val instanceof Object && !(val instanceof Date)) {

      return (
        (0, Object.keys)(val)
          .sort()
          /* sort to prevent SSR issues on pre-rendered sorted tables */
          .filter(function (v) {
            return v !== undefined && v !== null;
          })
          /* ignore undefined/null values */
          .map(function (k) {
            return UtilityClass.stringifyObjectValues(val[k]);
          })
          .join(" ")
      );
    }

    return String(val);
  }

  static SerachArrayofObjs(array, key, value) {
    var found = array.find(function (element) {
      return element[key] == value;
    });
    if (found) {
      return found;
    } else {
      return false;
    }
  }

  static getObjectFromArray(array, key, value) {
    var returned = {};
    for (var i = 0; i < array.length; i++) {
      if (array[i][key] == value) return array[i];
    }

    return returned;
  }

  static RandomItemFromArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      let j = Math.floor(Math.random() * (i + 1));
      let temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
    return array[0];
  }

  static isPromise(obj) {
    return (
      !!obj &&
      (typeof obj === "object" || typeof obj === "function") &&
      typeof obj.then === "function"
    );
  }

  /**
   * Internal function used to implement `utilsClass.throttle` and `utilsClass.debounce`.
   * @param {Function} func: function to be invoked.
   * @param {number} wait: The amount of milliseconds to wait before executing the said function.
   *
   * Borrowed from https://github.com/jashkenas/underscore/commit/9e3e067f5025dbe5e93ed784f93b233882ca0ffe
   */
  static limit(func, wait, debounce) {
    var timeout;

    function throtBounce() {
      var context = this,
        args = arguments;
      var throttler = function () {
        timeout = undefined;
        func.apply(context, args);
      };
      //The first ever time this function will be called, timeout will be null
      //This first cleartimeout will clear nothing, subsequently, it will be clearing any setup
      //callback awaiting execution. Uses Javascript event loop
      if (debounce) window.clearTimeout(timeout);
      //The case of !timeout is to invoke the function just once for case of throttle
      if (debounce || !timeout) timeout = window.setTimeout(throttler, wait);
    }
    throtBounce.clear = () => window.clearTimeout(timeout);
    return throtBounce;
  }

  /**
   *  Returns a function, that, when invoked, will only be triggered at most once
   *  during a given window of time.
   *
   *  TODO: allow to set if this callback should be invoked at the
   *            "Beginning" or "End" of the time out
   *            Currently it is invoked at the end
   */
  static throttle(func, wait) {
    return UtilityClass.limit(func, wait, false);
  }
  /**
   * Returns a "function"(rememeber to implement the function), that,
   * as long as it continues to be invoked, will not
   * be triggered. The function will be called after it stops being called for
   * N milliseconds.
   */
  static debounce(func, wait) {
    return UtilityClass.limit(func, wait, true);
  }

  static toogleFullscreen(htmlelement) {
    if (UtilityClass.isElementOnFullScreen()) {
      UtilityClass.exitFullScreen(htmlelement);
    } else {
      UtilityClass.EnterFullScreen(htmlelement);
    }
  }

  static isElementOnFullScreen() {
    // fullscreenElement webkitFullscreenElement   mozFullScreenElement   msFullscreenElement

    let isInFullScreen =
      (document.fullscreenElement && document.fullscreenElement !== null) ||
      (document.msFullscreenElement && document.msFullscreenElement !== null) ||
      (document.mozFullScreenElement &&
        document.mozFullScreenElement !== null) ||
      (document.webkitFullscreenElement &&
        document.webkitFullscreenElement !== null);

    return isInFullScreen;
  }

  static isFullscreenEnabled() {
    let isenabled =
      Document.fullscreenEnabled ||
      Document.webkitFullscreenEnabled ||
      Document.mozFullScreenEnabled ||
      Document.msFullscreenEnabled;

    return isenabled;
  }

  static isArrayLike(string) {
    return string.constructor == Array || string instanceof Array;
  }

  static isStringLike(string) {
    return typeof string == "string";
  }

  static pmsColor() {
    return "#1d8a99";
  }

  static agoColor() {
    return "#c5b451";
  }

  static dpkColor() {
    return "#360568";
  }

  static getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  static isEmptyObject(obj) {
    /* eslint-disable no-unused-vars */
    // See https://github.com/eslint/eslint/issues/6125
    var name;

    for (name in obj) {
      return false;
    }
    return true;
  }

  /**
   * @typedef {<T>(input: T) => T} DeepClone
   */
  /**
   *
   * @type {DeepClone}
   */
  static deepCloneWithJSON(input) {
    return JSON.parse(JSON.stringify(input));
  }

  static ShiftFirst(arr) {
    for (let i in arr) {
      // return the first element
      return arr[i];
    }
    return;
  }

  static DaysBetween(date1, date2) {
    //Get 1 day in milliseconds
    var one_day = 1000 * 60 * 60 * 24;

    // Convert both dates to milliseconds
    var date1_ms = date1.getTime();
    var date2_ms = date2.getTime();

    // Calculate the difference in milliseconds
    var difference_ms = date2_ms - date1_ms;
    //take out milliseconds
    difference_ms = difference_ms / 1000;

    var seconds = Math.floor(difference_ms % 60);

    difference_ms = difference_ms / 60;
    var minutes = Math.floor(difference_ms % 60);

    difference_ms = difference_ms / 60;
    var hours = Math.floor(difference_ms % 24);
    var days = Math.floor(difference_ms / 24);

    return { days, hours, seconds, minutes };
  }

  static convertHourstoDuration(hour_value) {
    return Math.round(hour_value * 60);
  }

  static insertComma(data) {
    if (data === 0) {
      return data;
    }
    data = String(data).split(".");
    let output = data[0].split("").reverse().join("");
    let result = [];

    output.split("").forEach((value, key) => {
      key += 1;
      if (key % 3 === 0) {
        result.push(value);
        result.push(",");
      } else {
        result.push(value);
      }
    });
    result = result.reverse().join("");
    if (data[1]) {
      if (result.startsWith(",")) {
        return result.slice(1) + `.${data[1]}`;
      }
      return result + `.${data[1]}`;
    } else {
      if (result.startsWith(",")) {
        return result.slice(1);
      }
      try {
        return result.reverse().join("");
      } catch (_) {
        return result;
      }
    }
  }

  static reformatDate(dateStr) {
    //i.e. convert  21-11-26 03:01:56 PM to 26/11/21 03:01:56 PM
    let firstSplittedDate = dateStr.split(" ");
    let reArrange = firstSplittedDate[0];
    let dateArray = reArrange.split("-");
    return (
      dateArray[2] +
      "/" +
      dateArray[1] +
      "/" +
      dateArray[0] +
      " " +
      firstSplittedDate[1] +
      " " +
      firstSplittedDate[2]
    );
  }
  //2022-04-20 14:54:08
  static formatDate2(initialStr) {
    if (initialStr == "N/A") {
      return "N/A";
    }
    //i.e. convert  2021-10-21T16:12:48 to 21/10/2021 4:12 PM
    let splitedStr = initialStr.split("T");
    const timeString = splitedStr[1];
    const timeStringTo12hr = new Date(
      "1970-01-01T" + timeString + "Z"
    ).toLocaleTimeString("en-US", {
      timeZone: "UTC",
      hour12: true,
      hour: "numeric",
      minute: "numeric",
    });

    const dateArray = splitedStr[0].split("-");
    const dateArrayFormated =
      dateArray[2] + "/" + dateArray[1] + "/" + dateArray[0];
    return `${dateArrayFormated} ${timeStringTo12hr} `;
  }
  static convertHourNumberToTimeInterval(passed_number) {
    if (passed_number == 0) {
      return "12AM - 1AM";
    } else if (passed_number == 1) {
      return "1AM - 2AM";
    } else if (passed_number == 2) {
      return "2AM - 3AM";
    } else if (passed_number == 3) {
      return "3AM - 4AM";
    } else if (passed_number == 4) {
      return "4AM - 5AM";
    } else if (passed_number == 5) {
      return "5AM - 6AM";
    } else if (passed_number == 6) {
      return "6AM - 7AM";
    } else if (passed_number == 7) {
      return "7AM - 8AM";
    } else if (passed_number == 8) {
      return "8AM - 9AM";
    } else if (passed_number == 9) {
      return "9AM - 10AM";
    } else if (passed_number == 10) {
      return "10AM - 11AM";
    } else if (passed_number == 11) {
      return "11AM - 12PM";
    } else if (passed_number == 12) {
      return "12PM - 1PM";
    } else if (passed_number == 13) {
      return "1PM - 2PM";
    } else if (passed_number == 14) {
      return "2PM - 3PM";
    } else if (passed_number == 15) {
      return "3PM - 4PM";
    } else if (passed_number == 16) {
      return "4PM - 5PM";
    } else if (passed_number == 17) {
      return "5PM - 6PM";
    } else if (passed_number == 18) {
      return "6PM - 7PM";
    } else if (passed_number == 19) {
      return "7PM - 8PM";
    } else if (passed_number == 20) {
      return "8PM - 9PM";
    } else if (passed_number == 21) {
      return "9PM - 10PM";
    } else if (passed_number == 22) {
      return "10PM - 11M";
    } else if (passed_number == 23) {
      return "11PM - 12AM";
    }
  }

  static extractNozzlesFromPumps(all_pumps) {
    let extractedNozzles = [
      ...all_pumps
        .reduce((r, { nozzles }) => {
          (nozzles || []).forEach((obj) => {
            r.has(obj.id) || r.set(obj.id, { ...obj });
          });

          return r;
        }, new Map())
        .values(),
    ];
    //console.log("extractNozzles", extractedNozzles);
    return extractedNozzles;
  }
}

export default UtilityClass;
