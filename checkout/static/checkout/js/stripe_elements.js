
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1)
var client_secret = $('#client_secret').text().slice(1, -1)

var stripe = Stripe(stripe_public_key);

var elements = stripe.elements();
var style = {
  base: {
    color: "#32325d",
      fontFamily: '"Josefin Slab", Arial, sans-serif',
      fontSmoothing: "antialiased",
      fontSize: "16px",
      "::placeholder": {
        color: "#aab7c4"
      }
    },
    invalid: {
      color: "#ff0000" ,
      iconColor: "#ff0000"
  }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.addEventListener('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
      var html = `
            <span role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(displayError).html(html);
  } else {
    displayError.textContent = '';
  }
});