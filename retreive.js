chrome.storage.sync.get(['openaiKey'], function(result) {
    var openaiKey = result.openaiKey;
    displayOpenAIKey(openaiKey);
});

function displayOpenAIKey(openaiKey) {
    var openaiKeyContainer = document.getElementById('openaiKeyContainer');
    openaiKeyContainer.textContent = "OpenAI Key: " + openaiKey;
}
  