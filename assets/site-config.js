/* CRRE Labs public site config
   This is the ONE place for the Google rating, review count, profile URL, and review quotes.

   googleReviewsUrl is the link for both "See our Google reviews" and "Leave us a Google review".
   TODO: replace googleBusinessProfileUrl with the Google Business Profile / Maps URL.
         That value is what sameAs uses. Do not put the review URL in sameAs.
   TODO: replace each reviews[] entry with a vetted Google review.
         Leave the PLACEHOLDER text until the quote is real.
         Do not publish invented testimonials.
*/
window.CRRE_SITE = {
  googleRating: "5.0",
  googleReviewCount: 24,
  googleBusinessProfileUrl: "TODO_GBP_URL",
  googleReviewsUrl: "https://g.page/r/CVrw8wHphIngEAI/review",
  reviews: [
    { quote: "PLACEHOLDER", author: "PLACEHOLDER", detail: "PLACEHOLDER" },
    { quote: "PLACEHOLDER", author: "PLACEHOLDER", detail: "PLACEHOLDER" },
    { quote: "PLACEHOLDER", author: "PLACEHOLDER", detail: "PLACEHOLDER" }
  ]
};
