import React, { useState } from "react";

function About() {
  const [highlightedSection, setHighlightedSection] = useState(null);

  const handleMouseEnter = (section) => {
    setHighlightedSection(section);
  };

  const handleMouseLeave = () => {
    setHighlightedSection(null);
  };

  return (
    <div className="about-section">
      <div className="about-content">
        <h1 className="about-title">About VISTA</h1>
        <p className="about-intro">
          Welcome to <strong>VISTA</strong>, the <em>Visual Identification of Significant Travel Attractions</em>.
          VISTA revolutionizes how tourists discover authentic and relevant information about destinations on Instagram by leveraging
          advanced <strong>deep learning</strong> and <strong>active learning</strong> techniques.
        </p>
        <div
          className={`about-details ${
            highlightedSection === "details" ? "highlighted" : ""
          }`}
          onMouseEnter={() => handleMouseEnter("details")}
          onMouseLeave={handleMouseLeave}
        >
          <h2>What We Do</h2>
          <p>
            VISTA automatically classifies photos into <strong>‘Tourism-Related’</strong> and <strong>‘Non-Tourism-Related’</strong> categories,
            helping users filter out irrelevant content. Trained on a robust dataset of the 10 most popular Israeli cities,
            our system achieves remarkable accuracy of <strong>96.5%</strong> and a weighted F1 score of <strong>96.4%</strong>.
          </p>
        </div>
        <div
          className={`about-performance ${
            highlightedSection === "performance" ? "highlighted" : ""
          }`}
          onMouseEnter={() => handleMouseEnter("performance")}
          onMouseLeave={handleMouseLeave}
        >
          <h2>Global Impact</h2>
          <p>
            Tested on the InstaCities100K dataset, VISTA demonstrated its global generalization capabilities with an accuracy of <strong>95.8%</strong>
            and a weighted F1 score of <strong>95.9%</strong>. These results confirm its effectiveness in identifying meaningful tourism content worldwide.
          </p>
        </div>
        <div
          className={`about-highlights ${
            highlightedSection === "highlights" ? "highlighted" : ""
          }`}
          onMouseEnter={() => handleMouseEnter("highlights")}
          onMouseLeave={handleMouseLeave}
        >
          <h2>Why Choose VISTA?</h2>
          <ul>
            <li>Filters out irrelevant content to highlight key travel insights.</li>
            <li>Engages users with high-quality tourism-related photos.</li>
            <li>Simplifies the travel planning process by curating relevant information.</li>
          </ul>
        </div>
        <p className="about-summary">
          With VISTA tourists can navigate Instagram’s overwhelming content and find authentic, valuable insights that enhance their travel experience.
        </p>
      </div>
    </div>
  );
}

export default About;