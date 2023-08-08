document.addEventListener('DOMContentLoaded', function() {
    var currentLinkBtn = document.getElementById('currentLinkBtn');
    
    currentLinkBtn.addEventListener('click', function(event) {
        event.preventDefault();
        var currentPageLink;
        
        // Get current page URL
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            currentPageLink = tabs[0].url;
        });

        // Show loading animation when the button is clicked
        var loadingContainer = document.getElementById('loading-container');
        loadingContainer.style.display = 'block';

        chrome.storage.sync.get(['openaiKey'], function(result) {
            var openaiKey = result.openaiKey;
            displayOpenAIKey(openaiKey, currentPageLink);
        });
      
    });
});
  
// Send request to Flask server
function displayOpenAIKey(openaiKey, currentPageLink) {

    // Hide the loading animation
    var loadingContainer = document.getElementById('loading-container');
    var summaryContainer = document.getElementById('summary-container');

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

            // Hide the loading animation
            loadingContainer.style.display = 'none';

            // Hide the button when it is clicked
            currentLinkBtn.style.display = 'none';

            summaryContainer.innerHTML = data;

        })
        .catch(error => {
            // Hide the loading animation and display an error message on failure
            loadingContainer.style.display = 'none';

            summaryContainer.innerHTML = error;
        });
    }
}
  
