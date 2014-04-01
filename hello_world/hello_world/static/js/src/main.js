                    var context,
                        settings = {
                            id: 'keyboard',
                            width: 735,
                            height: 200,
                            startNote: 'F4',
                            whiteNotesColour: 'white',
                            blackNotesColour: 'black',
                            hoverColour: '#820000',
                            octaves: 2
                        },
                        keyboard = new QwertyHancock(settings);
                    
                    if (typeof AudioContext === 'function') {
                        context = new AudioContext();
                    } else {
                        context = new webkitAudioContext();
                    }
                    
                    masterGain = context.createGain(),
                    nodes = [];
                    
                    masterGain.gain.value = 0.75;
                    masterGain.connect(context.destination);
                    
                    keyboard.keyDown = function (note, frequency) {
                        var oscillator = context.createOscillator();
                        oscillator.type = 3;
                        oscillator.frequency.value = frequency;
                        oscillator.connect(masterGain);
                        oscillator.start(0);
                    
                        nodes.push(oscillator);
                    };
                    
                    keyboard.keyUp = function (note, frequency) {
                        var new_nodes = [];
                    
                        for (var i = 0; i < nodes.length; i++) {
                            if (Math.round(nodes[i].frequency.value) === Math.round(frequency)) {
                                nodes[i].stop(0);
                                nodes[i].disconnect();
                            } else {
                                new_nodes.push(nodes[i]);
                            }
                        }
                    
                        nodes = new_nodes;
                    };