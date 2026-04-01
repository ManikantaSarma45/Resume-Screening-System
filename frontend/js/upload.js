// =========================
// ✅ BASE URLS
// =========================
const API_BASE = "http://127.0.0.1:8000/api/v1"; // 🔥 FIXED
const FILE_BASE = "http://127.0.0.1:8000";       // for PDF preview

// =========================
// ✅ LOAD ALL RESUMES (TABLE VIEW)
// =========================
function loadResumes() {
    fetch(`${API_BASE}/resumes/`)
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById("resume-list");
            container.innerHTML = "";

            if (!data.length) {
                container.innerHTML = `
                <tr>
                    <td colspan="4" class="p-4 text-center">
                        No resumes uploaded yet.
                    </td>
                </tr>
                `;
                return;
            }

            data.forEach(resume => {
                const row = document.createElement("tr");
                row.className = "border-b";

                row.innerHTML = `
                    <td class="p-3">${resume.id}</td>
                    <td class="p-3 font-medium">${resume.filename}</td>
                    <td class="p-3">
                        ${resume.content ? resume.content.substring(0, 50) : "No content"}...
                    </td>
                    <td class="p-3">
                        <a
                            href="${FILE_BASE}/uploads/${resume.filename}"
                            target="_blank"
                            class="text-blue-500 underline"
                        >
                            View
                        </a>
                    </td>
                `;

                container.appendChild(row);
            });
        })
        .catch(err => {
            console.error("Error loading resumes:", err);
        });
}

// =========================
// ✅ UPLOAD RESUME
// =========================
function uploadResume() {
    const fileInput = document.getElementById("resume-file");
    const status = document.getElementById("status");

    if (!fileInput.files.length) {
        status.innerText = "Please select a file ❗";
        status.className = "mt-4 text-red-600 font-medium";
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    // 🔵 Uploading state
    status.innerText = "Uploading...";
    status.className = "mt-4 text-blue-600 font-medium";

    fetch(`${API_BASE}/resumes/upload`, {
        method: "POST",
        body: formData
    })
        .then(async res => {
            if (!res.ok) {
                const errText = await res.text();
                throw new Error(errText);
            }
            return res.json();
        })
        .then(data => {
            console.log("Uploaded:", data);

            // ✅ SUCCESS
            status.innerText = `✅ ${data.filename} uploaded successfully`;
            status.className = "mt-4 text-green-600 font-medium";

            fileInput.value = "";

            // Reload list
            loadResumes();
        })
        .catch(err => {
            console.error("Upload failed:", err);

            status.innerText = "❌ Upload failed. Try again.";
            status.className = "mt-4 text-red-600 font-medium";
        });
}

// =========================
// ✅ AUTO LOAD
// =========================
window.onload = () => {
    loadResumes();
};