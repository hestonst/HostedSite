To run:
1) have python installed on your machine
2) type "cd path/to/the/root/of/this/github (e.g. cd ~/Desktop/HostedSite-main/ if it's on your desktop)"
  2a) note you can either download this git repository on the github website via a zip download link (top right) or cd to a directory and run "git checkout https://github.com/hestonst/HostedSite"
3) run python --version in your terminal
  3a) If python 3.x.x run "python -m http.server"
  3b) If python 2.x.x run "python -m SimpleHTTPServer 8000"
4) Go to the link in your browser that it prints to your terminal
5) You're done! As you change the html and css file your browser should reload those resources automatically as you save them to your disk without clearing cache in the browser since I'm magic (and also the CSS is within the HTML file)
