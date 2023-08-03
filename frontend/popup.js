// Get openai token
chrome.storage.sync.get(['openaiKey'], function(result) {
    var openaiKey = result.openaiKey;
    if (openaiKey) {
        // Key already set, redirect to home.html
        window.location.href = "summary.html";
    }
});

// Store openai token
document.getElementById('keyForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var openaiKey = document.getElementById('openaiKey').value;
    chrome.storage.sync.set({ 'openaiKey': openaiKey }, function() {
        console.log('OpenAI Key saved:', openaiKey);
    });

    // Redirect to welcome.html after saving the key
    window.close();
});
  
  