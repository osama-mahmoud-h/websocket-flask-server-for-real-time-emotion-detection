import { useEffect, useState } from "react";
import axios from 'axios';

export default function HttpCall() {
  const [data, setData] = useState("");

  useEffect(() => {
    axios.get("/http-call", {
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        console.log("data:  ",response.data.data);
        setData(response.data.data);
      })
      .catch((error) => {
        console.error("http-call error: ",error);
      });
  }, []); // Add an empty dependency array to only run once on mount

  return (
    <>
      <h2>HTTP Communication</h2>
      <h3 className="http">{data}</h3>
    </>
  );
}