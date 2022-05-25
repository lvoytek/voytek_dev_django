/**
 * MIT License
 *
 * Copyright (c) 2020 Lena Voytek
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 * Document: main.js
 *
 * Overview: This document contains functions and scripts that can be run by
 * any webpage on the site.
 */


function setColorMode(dark) {
  if (dark) {
    $("#style-dark").attr('rel', "stylesheet");
    $("#style-light").attr('rel', "stylesheet alternate");
  }
  else {
    $("#style-light").attr('rel', "stylesheet");
    $("#style-dark").attr('rel', "stylesheet alternate");
  }
}

function getAdditionalSidenavItems() {
  if (window.localStorage.getItem("authToken")) {
    $.ajax({
      url: '/additionalsidenavitems',
      type: 'GET',
      headers: { 'x-auth': window.localStorage.getItem("authToken") },
      dataType: 'json'
    })
      .done(addlSidenavSuccess);
  }
}

function addlSidenavSuccess(data, textSatus, jqXHR) {
  $('#slide-out').append(data.html);
  $("#proj-editor-link").click(function () {
    $.ajax(
      {
        url: "/projects-editor",
        beforeSend: function (xhr) { xhr.setRequestHeader('x-auth', window.localStorage.getItem("authToken")); },
        type: "GET",
        success: function (result) { window.document.write(result); }
      });
  });
}


$(document).ready(function () {
  //Activate/disable dark mode
  if (window.localStorage.getItem('darkModeOn') !== null) {
    $("#darkmode:checkbox").prop("checked", window.localStorage.getItem('darkModeOn') === "true");
    setColorMode(window.localStorage.getItem('darkModeOn') === "true");
  }
  else {
    window.localStorage.setItem('darkModeOn', "true");
  }

  //Check for currently active page in navbar
  $("#link-" + $("title").html()).addClass("active");

  getAdditionalSidenavItems();

  //Edit dark mode when checkbox toggled
  $("#darkmode").change(function () {
    if (this.checked) {
      window.localStorage.setItem('darkModeOn', "true");
    }
    else {
      window.localStorage.setItem('darkModeOn', "false");
    }

    setColorMode(this.checked);
  });
});
