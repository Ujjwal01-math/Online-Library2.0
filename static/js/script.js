let books = JSON.parse(localStorage.getItem("books")) || [];

// ✅ Add Book manually
function addBook(){

let name = document.getElementById("bookName").value;
let author = document.getElementById("authorName").value;

if(name=="" || author==""){
alert("Enter book details");
return;
}

let book={
name:name,
author:author,
status:"Available",
pdf: ""
};

books.push(book);

localStorage.setItem("books",JSON.stringify(books));

alert("Book Added");

document.getElementById("bookName").value="";
document.getElementById("authorName").value="";
}

// ✅ Show Books in table
function showBooks(){

let table = document.getElementById("bookTable");

if(!table) return;

books = JSON.parse(localStorage.getItem("books")) || [];

table.innerHTML = "";

books.forEach((book,index)=>{

table.innerHTML += `

<tr>
<td>${book.name}</td>
<td>${book.author}</td>
<td>${book.status}</td>

<td>

<button onclick="toggleStatus(${index})">Issue/Return</button>

<button onclick="deleteBook(${index})">Delete</button>

${book.status === "Issued" && book.pdf && book.pdf !=="undefined"? 
`<a href="${book.pdf}" target="_blank">
<button>View</button>
</a>` 
: ""}

</td>

</tr>

`;

});
}
// ✅ Toggle status
function toggleStatus(i){

books = JSON.parse(localStorage.getItem("books")) || [];

if(books[i].status=="Available")
books[i].status="Issued";
else
books[i].status="Available";

localStorage.setItem("books",JSON.stringify(books));

showBooks();
}

// ✅ Delete book
function deleteBook(i){

books = JSON.parse(localStorage.getItem("books")) || [];

books.splice(i,1);

localStorage.setItem("books",JSON.stringify(books));

showBooks();
}

// ✅ Search book
function searchBook(){

let input=document.getElementById("search").value.toLowerCase();

let rows=document.querySelectorAll("#bookTable tr");

rows.forEach(row=>{

let text=row.innerText.toLowerCase();

row.style.display=text.includes(input)?"":"none";

});
}

// 🔥 NEW: Issue from card (IMPORTANT)
function issueBook(name, author,pdf){

let books = JSON.parse(localStorage.getItem("books")) || [];

let newBook = {
    name: name,
    author: author,
    status: "Issued",
    pdf:pdf || ""
};

// duplicate avoid
let exists = books.some(b => b.name === name);

if(!exists){
    books.push(newBook);
}

localStorage.setItem("books", JSON.stringify(books));

// redirect to book list page
window.location.href = "/books/";
}