console.log('hello world')

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Assuming you have a function to capture the location on the client side
function captureLocation() {
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                resolve(`${latitude},${longitude}`);
            },
            (error) => {
                reject(error);
            }
        );
    });
}

const csrftoken = getCookie('csrftoken');

const video = document.getElementById('video-element')
const image = document.getElementById('img-element')
const captureBtn = document.getElementById('capture-btn')
const reloadBtn = document.getElementById('reload-btn')

reloadBtn.addEventListener('click', () => {
    window.location.reload()
})

// if (navigator.mediaDevices.getUserMedia) {
//     navigator.mediaDevices.getUserMedia({
//             video: true
//         })
//         .then((stream) => {
//             video.srcObject = stream
//             const {
//                 height,
//                 width
//             } = stream.getTracks()[0].getSettings()

//             captureBtn.addEventListener('click', e => {
//                 e.preventDefault()
//                 captureBtn.classList.add('not-visible')
//                 const track = stream.getVideoTracks()[0]
//                 const imageCapture = new ImageCapture(track)
//                 console.log(imageCapture)

//                 imageCapture.takePhoto().then(blob => {
//                     console.log("took photo:", blob)
//                     const img = new Image(width, height)
//                     img.src = URL.createObjectURL(blob)
//                     image.append(img)

//                     video.classList.add('not-visible')
//                     image.classList.add('taken-picture')

//                     const reader = new FileReader()

//                     reader.readAsDataURL(blob)
//                     reader.onloadend = () => {
//                         const base64data = reader.result
//                         console.log(base64data)

//                         const fd = new FormData()
//                         fd.append('csrfmiddlewaretoken', csrftoken)
//                         fd.append('foto_hadir', base64data)

//                         // Append location data to FormData

//                         $.ajax({
//                             type: 'POST',
//                             url: 'classify/',
//                             enctype: 'multipart/form-data',
//                             data: fd,
//                             processData: false,
//                             contentType: false,
//                             success: (resp) => {
//                                 console.log(resp)
//                                 window.location.href = resp.redirect_url
//                             },
//                             error: (err) => {
//                                 console.log(err)
//                             }
//                         })
//                     }
//                 }).catch(error => {
//                     console.log('takePhoto() error: ', error);
//                 });
//             });
//         })
//         .catch(error => {
//             console.log("Something went wrong!", error);
//         });
// }

if (navigator.mediaDevices.getUserMedia && navigator.geolocation.getCurrentPosition) {
    navigator.mediaDevices.getUserMedia({
            video: true
        })
        .then(async (stream) => {
            video.srcObject = stream;
            const {
                height,
                width
            } = stream.getTracks()[0].getSettings();

            try {
                // Capture location
                const location = await captureLocation();

                captureBtn.addEventListener('click', e => {
                    e.preventDefault();
                    captureBtn.classList.add('not-visible');
                    const track = stream.getVideoTracks()[0];
                    const imageCapture = new ImageCapture(track);
                    console.log(imageCapture);

                    imageCapture.takePhoto().then(blob => {
                        console.log("took photo:", blob);
                        const img = new Image(width, height);
                        img.src = URL.createObjectURL(blob);
                        image.append(img);

                        video.classList.add('not-visible');
                        image.classList.add('taken-picture');

                        const reader = new FileReader();

                        reader.readAsDataURL(blob);
                        reader.onloadend = () => {
                            const base64data = reader.result;
                            console.log(base64data);

                            const fd = new FormData();
                            fd.append('csrfmiddlewaretoken', csrftoken);
                            fd.append('foto_hadir', base64data);

                            // Check if location is available before appending to FormData
                            if (location) {
                                const [latitude, longitude] = location.split(',');
                                fd.append('latitude', parseFloat(latitude));
                                fd.append('longitude', parseFloat(longitude));
                            }

                            $.ajax({
                                type: 'POST',
                                url: 'classify/',
                                enctype: 'multipart/form-data',
                                data: fd,
                                processData: false,
                                contentType: false,
                                success: (resp) => {
                                    console.log(resp);
                                    window.location.href = resp.redirect_url;
                                },
                                error: (err) => {
                                    console.log(err);
                                }
                            });
                        };
                    }).catch(error => {
                        console.log('takePhoto() error: ', error);
                    });
                });
            } catch (error) {
                console.error('Error capturing location:', error);
            }
        })
        .catch(error => {
            console.log("Something went wrong!", error);
        });
}