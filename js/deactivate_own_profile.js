

async function deactivate_own_profile() {
    const current_url = window.location.href;
    const username_index = current_url.lastIndexOf("/") + 1;
    const username = current_url.substring(username_index);

    const frm = event.target.form;
    const formData = new FormData(frm);

    const conn = await fetch(`/deactivate-user/${username}`, {
        method: "POST",
        body: formData,
    });

    const data = await conn.json();

    if ( conn.ok && data.info == "ok" ) {

        // Redirect brugeren tilbage på forsiden
        fetch('/logout').then(response => {
            if (response.redirected) {
            window.location.href = response.url; // Redirect to the response URL
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

    } else {
        console.log("Cannot deactivate user");
    }
}

