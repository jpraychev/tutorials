console.log('===== Starting content script ======')
h1 = document.getElementsByTagName('h1')[0]
h1.innerHTML = 'Modified Example Domain'
console.log(`${h1} tag has been modified`)
console.log('===== Ending content script ======')