document.addEventListener('DOMContentLoaded', function() {

    // first hide all the divs, using display so the page accomodates itself
    document.querySelector('#tutor').style.display = 'none';
    document.querySelector('#student').style.display = 'none';

    document.querySelector('#select').onchange = function() {

        // get the option value and assign it to a variable
        let optionValue = this.value;

        // then show a certain div depending on wich value has the variable
        if (optionValue === 'tutor') {
                document.querySelector('#tutor').style.display = 'block';
                document.querySelector('#student').style.display = 'none';
            } else if (optionValue === 'student') {
                document.querySelector('#tutor').style.display = 'none';
                document.querySelector('#student').style.display = 'block';
            } else if (optionValue === 'empty') {
                document.querySelector('#tutor').style.display = 'none';
                document.querySelector('#student').style.display = 'none';
    }
};

})


