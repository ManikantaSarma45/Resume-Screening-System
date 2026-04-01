async function runRanking() {
    const jobId = document.getElementById("jobId").value;

    const res = await fetch(`http://127.0.0.1:8000/api/v1/ranking/rank/${jobId}`, {
        method: "POST"
    });

    const data = await res.json();

    let html = "";

    data.forEach(item => {
        html += `
        <div class="border p-3 mb-2">
            <p><strong>${item.filename}</strong></p>
            <p>Score: ${item.final_score}</p>
        </div>`;
    });

    document.getElementById("results").innerHTML = html;
}