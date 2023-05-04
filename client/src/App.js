import "./App.css";
import HttpCall from "./components/HttpCall";
import WebSocketCall from "./components/WebSocketCall";
import { io } from "socket.io-client";
import { useEffect, useRef, useState } from "react";

function App() {
  const socket = useRef();

  const [socketInstance, setSocketInstance] = useState("");
  const [loading, setLoading] = useState(true);
  const [buttonStatus, setButtonStatus] = useState(true);
  const[helloMessage,setHelloMessage] = useState("");

  const [image, setImage] = useState(null);
  const [fileData, setFileData] = useState(null);
  const [imageBuffer, setImageBuffer] = useState(null);


 

  useEffect(()=>{
    socket.current = io('/');

    socket.current.on("connect",(data)=>{
      console.log("connected wesocket data: ", data);
      setHelloMessage("hello websocket connectd ");
    });

    socket.current.on("result_file",(data)=>{
      console.log("result_file from wesocket data: ", data);
    });

    socket.current.on("result_file",(file)=>{
      setImageBuffer(file.image);
      console.log("new result image: ");
    });

  },[]);

  const handleFileInputChange = (event) => {
    const file = event.target.files[0];

    console.log(`Selected file size: ${file.size} bytes`);

    const reader = new FileReader();
    reader.onload = () => {
      const arrayBuffer = reader.result;
      const byteArray = new Uint8Array(arrayBuffer);
      setFileData(byteArray);
    };
    reader.readAsArrayBuffer(file);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    
    socket.current.emit("file",{
      fileData
    });
    console.log("file read: ",fileData);
    // Do something with fileData
  };
  
 
  return (
    <div className="App">
      <h1>React/Flask App + socket.io</h1>
      <div className="line">
        <HttpCall />
      </div>


    {helloMessage && helloMessage.length>0 ? 
    
    <div>
    {helloMessage}
  </div>
    :<></>
    }

 
<form onSubmit={handleSubmit}>
      <input type="file" accept="image/*" onChange={handleFileInputChange} />
      <button type="submit">Submit</button>
    </form>

    
    
    {imageBuffer && (
      <img src={`data:image/jpeg;base64,${btoa(String.fromCharCode(...new Uint8Array(imageBuffer)))}`} alt="uploaded" />
    )}
    
     


    </div>
  );
}

export default App;