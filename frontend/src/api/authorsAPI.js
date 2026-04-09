import { api } from "./api"

// GET
export const getAuthors=async()=>{
    const res=await api.get("authors/")
    return res.data.results || res.data
}

// CREATE author
export const createAuthor = async (data) => {
  return await api.post("authors/", data);
};

// DELETE author
export const deleteAuthor = async (id) => {
  return await api.delete(`authors/${id}/`);
};