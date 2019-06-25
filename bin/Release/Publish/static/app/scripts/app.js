

function appTest() {


    $.ajax({
        url: '/show/list',
        type: 'get',
        dataType: 'json',
        async: true,
        success: function (data) {
            var testVar = JSON.stringify(data) // turns object into string
            var testSplic = testVar.slice(10, -2) //formats the obeject string and removes things we dont need
            // var replace = testSplic.replace("{", "")
            //var newStr = replace
            // console.log(newStr)
            var str = testSplic.split(",") // turns strings to arrays at ,
            // var runOut = str//final string output
            console.log(testVar);



            var e = ('{"showTime":' + '"' + 10 + ':' + '00' + ':' + '00' + '"');
            //gets current time that matches the string in the final string otuput
            var f = testVar.includes(e) //checks to see if variable e exits in runOut string, which it does but it is not working correctly. It is now, var g needed to be defined before var f.
            console.log(e)
            console.log(f);


            // testing to see if I can combine the show times and show names
            //so far I can only get it to dispaly as array pairs in the log.
            //This needs to work so we know the appropriate popup to display

            var iterator = [data].values();

            for (var value of iterator) {
                var testArray1 =  //test    
                    console.log(value);
            }
            console.log(data);

            var shows = data.shows

            var time = new Date().toTimeString().replace(/.*(\d{2}:\d{2}:\d{2}).*/, "$1");
            //var time ="10:00:00"

            var findShow = (time, shows) => {
                var currentShows = [];
                for (let i = 0; i < shows.length; i++) {
                    if (shows[i].showTime && shows[i].showTime === time) {
                        currentShows.push(shows[i]);
                    }
                }
                return currentShows;
            }

            var findshows = findShow(time, shows)
            console.log(findshows)


            function getTime() {
                setInterval(function () {

                    var time = new Date().toTimeString().replace(/.*(\d{2}:\d{2}:\d{2}).*/, "$1");

                    var currentShows = findShow(time, shows);
                    if (currentShows.length) {

                        for (let i = 0; i < currentShows.length; i++) {
                            Push.create(currentShows[i].showMessage, {
                                body: currentShows[i].showName,
                                icon: '/icon.png',
                                timeout: 4000,
                                onClick: function () {
                                    window.focus();
                                    this.close();
                                }
                            })
                        }


                    }
                    
                    
                    4

                }, 1000);
            };
            getTime();


            

            function addZero(i) { //function adds leading zero to minutes and zero's if needed
                if (i < 10) {
                    i = "0" + i;
                }
                return i;
            }


        } //ends the success function

    }); //ends the ajax call

} //ends the appTest function
