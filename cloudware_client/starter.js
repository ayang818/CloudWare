const clipboard = require('clipboardy')


readCb = function() {
    try {
        content = clipboard.readSync() // maybe test/binary?
        console.log(content)
    } catch (error) {
        console.log('err=%s' % error)
    }
}

setInterval(readCb, 1000)
