import axios from "axios";

const api = axios.create({
  baseURL: "https://topsis-102317087-25yp.vercel.app/api",
});

export default api;
