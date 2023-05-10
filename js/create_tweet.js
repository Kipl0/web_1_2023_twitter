// Create tweet

async function tweet() {
    const frm = event.target.form;
    const conn = await fetch("/tweet", {
        method: "POST",
        body: new FormData(frm)
    });

    const data = await conn.json();

    if (!conn.ok) {
        const errorTip = document.getElementById("error-tip");
        errorTip.innerText = data.error; // Assuming the server returns an 'error' field in the response
        errorTip.style.display = "block";
        console.log(data.error)
        return;
    }

    location.reload();
}

