import * as React from "react";
import Box from "@mui/material/Box";
import Slider from "@mui/material/Slider";
import * as PropTypes from "prop-types";
import "../../scss/mapLegends.scss";

function valuetext(value) {
    return `${value}°C`;
}

export default function DiscreteSlider({handleSliderChange, marks}) {
    function handleChange(event, newValue) {
        handleSliderChange(newValue);
    }

    return (
        <Box
            class="timeline"
            style={{
                width: "100%",
                right: 0,
                display: "flex",
                justifyContent: "center",
                marginTop: "2%"
            }}
        >
            <Slider
                sx={{
                    "& .MuiSlider-markLabel": {
                        fontSize: "larger",
                        fontWeight: "bold",
                        opacity: "100%",
                        color: "black",
                        textShadow: "2px 0 0 #fff, 0 2px 0 #fff, -2px 0 0 #fff, 0 -2px 0 #fff"
                    },
                    "& .MuiSlider-rail": {
                        height: 12, // Increase the height of the track
                        borderRadius: 6,
                        backgroundColor: "black",
                        opacity: "40%"
                    },
                    "& .MuiSlider-thumb": {
                        width: 24, // Increase the width of the thumb
                        height: 24, // Increase the height of the thumb
                        backgroundColor: "darkRed"
                    },
                    "& .MuiSlider-track": {
                        color: "transparent" // Make the active part (track) transparent
                    }
                }}
                aria-label="Year"
                size="large"
                defaultValue={30}
                getAriaValueText={valuetext}
                valueLabelDisplay="auto"
                shiftStep={5}
                onChange={handleChange}
                step={5}
                marks={marks}
                min={2004}
                max={2019}
            />
        </Box>
    );
}

DiscreteSlider.propTypes = {
    handleSliderChange: PropTypes.func,
    marks: PropTypes.array
};
