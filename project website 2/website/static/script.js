document.addEventListener('DOMContentLoaded', function() {
  const gaugeElement = document.querySelector(".gauge");
   console.log("albert")
  function setGaugeValue(gauge, value) {
      if (value < 0 || value > 1) {
          return;
      }

      // Calculate the rotation based on the value
      const rotation = value * 180; // assuming a semi-circle gauge

      // Update the fill with the calculated rotation
      gauge.querySelector(".gauge__fill").style.transform = `rotate(${rotation}deg)`;
      gauge.querySelector(".gauge__cover").textContent = `${Math.round(value * 100)}%`;
  }

  function updateGaugeValue() {
      // Make an AJAX request to fetch the Arduino data
      fetch('/get_arduino_data')
          .then(response => response.json())
          console.log(data,"brian")
          .then(data => {
              if (data && data.data) {
                  const arduinoData = parseFloat(data.data); // Assuming arduinoData is a float value
                  setGaugeValue(gaugeElement, arduinoData);
              } else {
                  console.error('Error: No Arduino data received');
              }
          })
          .catch(error => console.error('Error fetching Arduino data:', error));
  }

  // Initial call to update gauge value
  updateGaugeValue();

  // Repeatedly call updateGaugeValue every second
  setInterval(updateGaugeValue, 1000); // 1 second interval
});
