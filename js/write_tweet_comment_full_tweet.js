/**
 * Denne funktion bliver kaldt en gang når js filen bliver importeret
 * - Formålet med dette er at lave kun en eventlistener.
 */
function comment_init() {
    // Hvis brugeren ønsker at lave kommentar med billede
    let uploaded_comment_img = "";
    const uploaded_comment_img_input = document.getElementById("uploaded_comment_img_input");

    uploaded_comment_img_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_comment_img = reader.result;
        document.getElementById("uploaded_comment_img").src = uploaded_comment_img;
    });
    reader.readAsDataURL(this.files[0]);
    });

}

// Kald når js filen bliver importeret
comment_init()