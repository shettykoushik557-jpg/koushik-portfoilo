document.addEventListener("DOMContentLoaded", function () {
    console.log("Portfolio JavaScript is working!");

    const contactLinks = document.querySelector(".contact-links");

    if (contactLinks) {
        contactLinks.addEventListener("click", function () {
            console.log("Contact link clicked!");
        });
    }
});