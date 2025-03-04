"use client"

import { useEffect, useState, useMemo } from "react"
import { useLocation } from "react-router-dom"

function ModelTest() {
  const location = useLocation()
  const [classifiedImages, setClassifiedImages] = useState({
    tourist: JSON.parse(localStorage.getItem("touristImages")) || [],
    nonTourist: JSON.parse(localStorage.getItem("nonTouristImages")) || [],
  })
  const [results, setResults] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  const imageUrls = useMemo(() => location.state?.imageUrls || [], [location.state?.imageUrls])

  useEffect(() => {
    if (imageUrls.length === 0) return

    const classifyImages = async () => {
      try {
        setIsLoading(true)
        const newResults = []

        for (const imageUrl of imageUrls) {
          const formData = new FormData()
          formData.append("image", await fetch(imageUrl).then((res) => res.blob()))

          const response = await fetch("http://127.0.0.1:8000/gallery/classify-image/", {
            method: "POST",
            body: formData,
          })

          if (response.ok) {
            const data = await response.json()
            newResults.push({
              imageUrl,
              classification: data.classification,
              confidence: (data.confidence * 100).toFixed(2),
            })

            setClassifiedImages((prev) => {
              const newImages = {
                tourist:
                  data.classification === "תיירות" && !prev.tourist.includes(imageUrl)
                    ? [...prev.tourist, imageUrl]
                    : prev.tourist,
                nonTourist:
                  data.classification === "לא תיירות" && !prev.nonTourist.includes(imageUrl)
                    ? [...prev.nonTourist, imageUrl]
                    : prev.nonTourist,
              }

              localStorage.setItem("touristImages", JSON.stringify(newImages.tourist))
              localStorage.setItem("nonTouristImages", JSON.stringify(newImages.nonTourist))

              return newImages
            })
          } else {
            newResults.push({ imageUrl, classification: "שגיאה", confidence: "N/A" })
          }
        }

        setResults(newResults)
      } catch (error) {
        console.error("שגיאה בסיווג התמונות:", error)
      } finally {
        setIsLoading(false)
      }
    }

    classifyImages()
  }, [imageUrls])

  // 🔹 פונקציה למחיקת כל התמונות מה-LocalStorage ומה-State
  const clearAllImages = () => {
    setClassifiedImages({ tourist: [], nonTourist: [] }) // 🔄 מנקה את ה-State
    localStorage.removeItem("touristImages") // 🔄 מוחק מה-LocalStorage
    localStorage.removeItem("nonTouristImages")
    setResults([]) // 🔄 מוחק גם את תוצאות הסיווג
    alert("✅ All images have been cleared!")
  }

  return (
    <div className="model-test">
      <div className="page-container">
        <h1 className="classification-title">Image Classification</h1>
        {isLoading && <p className="loading-text">Classifying images...</p>}

        {/* 🔹 כפתור לניקוי כל התמונות */}
        <button className="clear-all-button" onClick={clearAllImages}>
          🗑️ Clear All Images
        </button>

        <div className="classification-gallery">
          <div className="classification-column">
            <h2 className="column-title">🏝 Tourist</h2>
            <div className="image-grid">
              {classifiedImages.tourist.map((img, index) => (
                <img key={index} src={img || "/placeholder.svg"} alt="Tourist" className="classified-image" />
              ))}
            </div>
          </div>

          <div className="classification-column">
            <h2 className="column-title">🏠 Non-Tourist</h2>
            <div className="image-grid">
              {classifiedImages.nonTourist.map((img, index) => (
                <img key={index} src={img || "/placeholder.svg"} alt="Non-Tourist" className="classified-image" />
              ))}
            </div>
          </div>
        </div>

        <div className="results-container">
          {results.map((res, index) => (
            <div key={index} className="result-item">
              <img src={res.imageUrl || "/placeholder.svg"} alt={`Result ${index}`} className="classified-image" />
              <p>
                {res.classification === "תיירות" ? (
                  <span className="classification-icon success">✔ Tourist</span>
                ) : (
                  <span className="classification-icon error">❌ Non-Tourist</span>
                )}
              </p>
              <p className="confidence-text">
                Confidence: <strong>{res.confidence}%</strong>
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default ModelTest

