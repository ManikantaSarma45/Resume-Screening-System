async function createJob() {
    const body = {
        title: document.getElementById("title").value,
        description: document.getElementById("desc").value,
        must_have: document.getElementById("must").value,
        good_to_have: document.getElementById("good").value
    };

    const res = await fetch("http://localhost:8000/api/v1/jobs/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });

    const data = await res.json();

    document.getElementById("status").innerText = "Job Created ID: " + data.id;
}