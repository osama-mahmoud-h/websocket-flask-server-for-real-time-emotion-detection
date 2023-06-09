import { useEffect, useState } from "react";

export const useMediaDevice = (
    videoRef,
    canvasRef,
    period = 10000,
    options = { video: true }
) => {
    const [image, setImage] = useState(null);

    useEffect(() => {
        navigator.mediaDevices
            .getUserMedia(options)
            .then((stream) => {
                videoRef.current.srcObject = stream;
            })
            .catch((err) => {
                console.error(err);
            });
    }, [videoRef, options]);

    useEffect(() => {
        let interval = setInterval(() => {
            if (videoRef.current.readyState === 4) {
                canvasRef.current.getContext("2d").drawImage(videoRef.current, 0, 0);
                canvasRef.current.toBlob(
                    (blob) => {
                        // const file = new File([blob], "image.png", { type: "image/png" });
                        setImage(blob);
                    },
                    "image/png",
                    0.9
                );
            }
        }, period);

        return () => clearInterval(interval);
    }, [videoRef, canvasRef, period]);

    return image;
};
