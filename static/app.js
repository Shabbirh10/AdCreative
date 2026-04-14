// One-Click Generator Bridge
const elements = {
    form: document.getElementById("personalize-form"),
    upload: document.getElementById("upload-zone"),
    file: document.getElementById("file-input"),
    adUrl: document.getElementById("ad-url"),
    submit: document.getElementById("submit-btn"),
    overlay: document.getElementById("loading-overlay"),
    status: document.getElementById("loading-status"),
    previewArea: document.getElementById("preview-area"),
    resultsLog: document.getElementById("results-log"),
    logContent: document.getElementById("log-content"),
    iframe: document.getElementById("preview-iframe")
};

let state = {
    file: null,
    personalizedHtml: null,
    isProcessing: false
};

elements.upload.onclick = () => elements.file.click();

elements.file.onchange = (e) => {
    const file = e.target.files[0];
    if (file) {
        state.file = file;
        document.getElementById("file-info").textContent = `Ready: ${file.name}`;
        document.getElementById("file-info").style.display = "block";
        elements.adUrl.value = "";
    }
};

elements.form.onsubmit = async (e) => {
    e.preventDefault();
    if (state.isProcessing) return;

    const adUrl = elements.adUrl.value.trim();
    if (!state.file && !adUrl) return alert("Please provide an ad creative asset");

    startProcess();

    const formData = new FormData();
    if (state.file) formData.append("ad_image", state.file);
    if (adUrl) formData.append("ad_image_url", adUrl);

    try {
        log("INFO", "Initializing generation pipeline...");
        log("INFO", "Uploading asset to Vision engine...");
        
        const response = await fetch("/api/personalize", { method: "POST", body: formData });
        const data = await response.json();

        if (!response.ok) throw new Error(data.detail || "Generation failure");

        state.personalizedHtml = data.personalized_html;

        log("SUCCESS", "Creative analysis complete.");
        log("SUCCESS", "Optimal template selected.");
        log("SUCCESS", "Copywriting and styling complete.");
        
        displayResults();
    } catch (err) {
        log("ERROR", err.message);
        alert(err.message);
    } finally {
        endProcess();
    }
};

function log(level, msg) {
    const time = new Date().toLocaleTimeString();
    const line = document.createElement("div");
    line.style.marginBottom = "6px";
    line.innerHTML = `<span style="color: #6366f1;">[${time}]</span> <span style="font-weight: 600; color: ${level === 'ERROR' ? '#ef4444' : '#fff'};">${level}:</span> ${msg}`;
    elements.logContent.appendChild(line);
    elements.logContent.scrollTop = elements.logContent.scrollHeight;
}

function startProcess() {
    state.isProcessing = true;
    elements.submit.disabled = true;
    elements.overlay.style.display = "flex";
    elements.logContent.innerHTML = "";
    elements.resultsLog.style.display = "block";
    elements.previewArea.style.display = "none";
}

function endProcess() {
    state.isProcessing = false;
    elements.submit.disabled = false;
    elements.overlay.style.display = "none";
}

function displayResults() {
    elements.previewArea.style.display = "block";
    const doc = elements.iframe.contentDocument || elements.iframe.contentWindow.document;
    doc.open();
    doc.write(state.personalizedHtml);
    doc.close();
    elements.previewArea.scrollIntoView({ behavior: "smooth" });
}

function downloadHTML() {
    const blob = new Blob([state.personalizedHtml], { type: "text/html" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `landing-page-${Date.now()}.html`;
    a.click();
}

function openNewTab() {
    const win = window.open("", "_blank");
    win.document.write(state.personalizedHtml);
    win.document.close();
}
