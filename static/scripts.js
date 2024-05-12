// Fetch accuracy data from JSON file
fetch('accuracy.json')
  .then(response => response.json())
  .then(data => {
    // Update accuracy spans in HTML
    document.getElementById('rf-accuracy').innerText = data.random_forest.toFixed(2) + "%";
    document.getElementById('dt-accuracy').innerText = data.decision_tree.toFixed(2) + "%";
    document.getElementById('nb-accuracy').innerText = data.naive_bayes.toFixed(2) + "%";
    document.getElementById('mlp-accuracy').innerText = data.mlp.toFixed(2) + "%";
  })
  .catch(error => console.error('Error fetching accuracy data:', error));

  document.getElementById('predict-button').addEventListener('click', function() {
    var fileInput = document.getElementById('audio-file');
    var file = fileInput.files[0];

    var formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predicted-emotion').innerText = 'Predicted Emotion: ' + data.emotion;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
