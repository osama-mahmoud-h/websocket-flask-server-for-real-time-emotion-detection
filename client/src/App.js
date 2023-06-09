import "./App.css";
import HttpCall from "./components/HttpCall";
import { io } from "socket.io-client";
import { useEffect, useRef, useState } from "react";
import { useMediaDevice } from "./useMediaDevice";

function App() {
    const socket = useRef();
    const [helloMessage, setHelloMessage] = useState("");

    const videoRef = useRef();
    const canvasRef = useRef();
    const image = useMediaDevice(videoRef, canvasRef, 1000);

    const [fileData, setFileData] = useState(null);
    const [imageBuffer, setImageBuffer] = useState(null);

    useEffect(() => {
        if (!socket?.current?.connected) {
            socket.current = io("/");
            socket.current.on("connect", (data) => {
                console.log("connected wesocket data: ", data);
                setHelloMessage("hello websocket connectd ");
            });

            socket.current.on("result_file", (file) => {
                setImageBuffer(file.image);
                console.log("new result image: ");
            });
        }
    }, []);

    useEffect(() => {
        const reader = new FileReader();
        reader.onload = () => {
            const arrayBuffer = reader.result;
            const byteArray = new Uint8Array(arrayBuffer);
            setFileData(byteArray);
        };
        if (image) reader.readAsArrayBuffer(image);
    }, [image]);

    useEffect(() => {
        socket.current.emit("file", {
            fileData,
        });
        // console.log("file read: ", fileData);
    }, [fileData]);
    // const handleFileInputChange = (event) => {
    //     const file = event.target.files[0];

    //     console.log(`Selected file size: ${file.size} bytes`);

    //     const reader = new FileReader();
    //     reader.onload = () => {
    //         const arrayBuffer = reader.result;
    //         const byteArray = new Uint8Array(arrayBuffer);
    //         setFileData(byteArray);
    //     };
    //     reader.readAsArrayBuffer(file);
    // };

    // const handleSubmit = (event) => {
    //     event.preventDefault();

    //     socket.current.emit("file", {
    //         fileData,
    //     });
    //     console.log("file read: ", fileData);
    //     // Do something with fileData
    // };

    return (
        <div className="App">
            <h1>React/Flask App + socket.io</h1>
            <div className="line">
                <HttpCall />
            </div>

            {helloMessage && helloMessage.length > 0 ? <div>{helloMessage}</div> : <></>}

            {/* <form onSubmit={handleSubmit}>
                <input type="file" accept="image/*" onChange={handleFileInputChange} />
                <button type="submit">Submit</button>
            </form> */}

            {imageBuffer && (
                <img
                    src={`data:image/jpeg;base64,${btoa(
                        String.fromCharCode(...new Uint8Array(imageBuffer))
                    )}`}
                    alt="uploaded"
                />
            )}
            <video
                ref={videoRef}
                width="640"
                height="480"
                autoPlay
                style={{ display: "none" }}
            />
            <canvas ref={canvasRef} width="640" height="480" style={{ display: "none" }} />
        </div>
    );
}

export default App;
