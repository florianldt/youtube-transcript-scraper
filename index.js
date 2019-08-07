const express = require('express');

const app = express();
const morgan = require('morgan');
const fs = require('fs');

app.use(morgan('short'));

app.get("/subtitles/:videoId", (req, res) => {

    var spawn = require("child_process").spawn; 
      
    var process = spawn('python3',["./captions.py", 
                            req.params.videoId]); 
  
    process.stdout.on('data', function(data) { 

        let path = './tmp/tmp_' + req.params.videoId + '.json'

        fs.readFile(path, (err, data) => {

            if (err) throw err;
            let json = JSON.parse(data);
            
            if (json["success"] === true) {
                res.status(200).json(json["subtitles"]);
            } else {
                let jsonRes = { "message": json["msg"] }
                res.status(500).json(jsonRes);
            }

            try {
                fs.unlinkSync(path);
                console.log(path + 'removed');
            } catch(err) {
                console.error(err);
            }

        });
    }) 
});

app.listen(8080, () => {
    console.log('running...');
});