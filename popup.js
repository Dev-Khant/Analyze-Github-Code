document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('keyForm');
    var openaiKeyInput = document.getElementById('openaiKey');
  
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        saveOpenAIKey();
    });
  
    function saveOpenAIKey() {
        var openaiKey = openaiKeyInput.value;
        
        // Store the OpenAI key in Chrome storage
        chrome.storage.sync.set({ 'openaiKey': openaiKey }, function() {
            console.log('OpenAI Key saved:', openaiKey);

            // Redirect to welcome.html
            window.location.href = "welcome.html";
      });
    }
  });
  