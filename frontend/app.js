let datasetId = null;
const el = id => document.getElementById(id);
const pretty = obj => JSON.stringify(obj, null, 2);
el('upload').onclick = async () => {
  const file = el('file').files[0];
  if (!file) { el('status').textContent = 'Choose a CSV or XLSX file.'; return; }
  const form = new FormData(); form.append('file', file);
  el('status').textContent = 'Uploading...';
  try {
    const res = await fetch('/api/upload', { method: 'POST', body: form });
    const data = await res.json();
    if (!res.ok) throw Error(data.detail || 'Upload failed');
    datasetId = data.dataset_id;
    el('overview').textContent = pretty(data.profile);
    el('status').textContent = 'Dataset ready.';
    el('ask').disabled = false;
  } catch (err) { el('status').textContent = err.message; }
};
el('ask').onclick = async () => {
  if (!datasetId) return;
  el('answer').textContent = 'Analyzing...';
  try {
    const res = await fetch('/api/chat', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({dataset_id:datasetId,question:el('question').value}) });
    const data = await res.json();
    if (!res.ok) throw Error(data.detail || 'Analysis failed');
    el('answer').textContent = `${data.explanation}\n\nComputed results:\n${pretty(data.results.numeric_summary)}`;
  } catch (err) { el('answer').textContent = err.message; }
};
