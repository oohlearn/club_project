import { Routes, Route } from "react-router-dom";
import Home from "./pages/front/Homepage/Home";
import FrontLayout from "./pages/front/FontLayout";
import IntroPage from "./pages/front/Intro/Intro";
import Activities from "./pages/front/Activities/ActivitiesPage";
import ActivityTicket from "./pages/front/Activities/ActivityTicket";
import IntroHome from "./pages/front/Intro/IntroHome";
import ExperiencesPage from "./pages/front/Intro/Experiences";
import Conductors from "./pages/front/Intro/Conductors";
import Teachers from "./pages/front/Intro/Teachers";
import Videos from "./pages/front/Videos/VideosPage";
import Albums from "./pages/front/Albums/AlbumsPage";
import AlbumDetail from "./pages/front/Albums/AlbumDetail";
import News from "./pages/front/News/News";
import NewsDetail from "./pages/front/News/NewsDetail";
import Contact from "./pages/front/Contact";
import Shop from "./pages/front/Shop/ShopPage";
import ChooseSeats from "./pages/front/Order/ChooseSeats";
import Checkout from "./pages/front/Shop/Checkout";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<FrontLayout />}>
          <Route path="" element={<Home />}></Route>
          <Route path="intro" element={<IntroPage />}>
            <Route path="" element={<IntroHome />}></Route>
            <Route path="experiences" element={<ExperiencesPage />}></Route>
            <Route path="conductors" element={<Conductors />}></Route>
            <Route path="teachers" element={<Teachers />}></Route>
          </Route>
          <Route path="activities" element={<Activities />}></Route>
          <Route path="activities/:activityId" element={<ActivityTicket />}></Route>
          <Route path="activities/:activityId/choose_seats" element={<ChooseSeats />}></Route>
          <Route path="videos" element={<Videos />}></Route>
          <Route path="albums" element={<Albums />}></Route>
          <Route path="albums/:albumId" element={<AlbumDetail />}></Route>
          <Route path="news" element={<News />}></Route>
          <Route path="news/:newsId" element={<NewsDetail />}></Route>
          {/* Navbar */}
          <Route path="contact" element={<Contact />}></Route>
          <Route path="shop" element={<Shop />}></Route>
          <Route path="shop/checkout" element={<Checkout />}></Route>
        </Route>
      </Routes>
    </div>
  );
}

export default App;
