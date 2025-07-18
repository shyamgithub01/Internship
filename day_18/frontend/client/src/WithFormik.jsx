// // WithoutFormik.jsx
// import React, { useState } from "react";

// const WithoutFormik = () => {
//   const [formData, setFormData] = useState({ name: "", email: "" });

//   const handleChange = (e) => {
//     setFormData({ ...formData, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     alert(JSON.stringify(formData, null, 2));
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <label>Name:</label>
//       <input
//         type="text"
//         name="name"
//         value={formData.name}
//         onChange={handleChange}
//       />

//       <br />

//       <label>Email:</label>
//       <input
//         type="email"
//         name="email"
//         value={formData.email}
//         onChange={handleChange}
//       />

//       <br />

//       <button type="submit">Submit</button>
//     </form>
//   );
// };

// export default WithoutFormik;

// WithFormik.jsx
import React from "react";
import { Formik, Form, Field } from "formik";

const WithFormik = () => {
  return (
    <Formik
      initialValues={{ name: "", email: "" }}
      onSubmit={(values) => {
        alert(JSON.stringify(values, null, 2));
      }}
    >
      <Form>
        <label>Name:</label>
        <Field type="text" name="name" />

        <br />

        <label>Email:</label>
        <Field type="email" name="email" />

        <br />

        <button type="submit">Submit</button>
      </Form>
    </Formik>
  );
};

export default WithFormik;
