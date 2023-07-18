document.addEventListener('DOMContentLoaded', function() {
    var currentLinkBtn = document.getElementById('currentLinkBtn');
    
    currentLinkBtn.addEventListener('click', function(event) {
        event.preventDefault();
        var currentPageLink;
        
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            currentPageLink = tabs[0].url;
        });

        chrome.storage.sync.get(['openaiKey'], function(result) {
            var openaiKey = result.openaiKey;
            displayOpenAIKey(openaiKey, currentPageLink);
        });
      
    });
});
  

function displayOpenAIKey(openaiKey, currentPageLink) {
    var container = document.getElementById('summary-container');

    if (openaiKey) {
        fetch('http://localhost:8000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"openaiKey": openaiKey, "currentPageLink": currentPageLink})
            })
            .then(response => response.text())
            .then(data => {
        
            container.textContent = "Data :" + data;
        });
    }
}
  