function sendMail(contactForm) {
    emailjs.send("gmail", "cookbook-blog", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "recipe_idea": contactForm.recipeidea.value
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    // return false;  // can use this to send a feedback message, set time out etc, after success
}
