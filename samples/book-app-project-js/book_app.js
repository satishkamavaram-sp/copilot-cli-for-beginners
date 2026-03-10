const readline = require("readline");
const { BookCollection } = require("./books");

const collection = new BookCollection();

function showBooks(books) {
  if (!books || books.length === 0) {
    console.log("No books found.");
    return;
  }

  console.log("\nYour Book Collection:\n");

  books.forEach((book, index) => {
    const status = book.read ? "✓" : " ";
    console.log(`${index + 1}. [${status}] ${book.title} by ${book.author} (${book.year})`);
  });

  console.log();
}

function handleList() {
  const books = collection.listBooks();
  showBooks(books);
}

function prompt(question) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer.trim());
    });
  });
}

async function handleAdd() {
  console.log("\nAdd a New Book\n");

  const title = await prompt("Title: ");
  const author = await prompt("Author: ");
  const yearStr = await prompt("Year: ");

  try {
    const year = yearStr ? parseInt(yearStr, 10) : 0;
    if (isNaN(year)) {
      throw new Error("That doesn't look like a year. Please enter a number, like 1999.");
    }
    collection.addBook(title, author, year);
    console.log("\nBook added successfully.\n");
  } catch (err) {
    console.log(`\nError: ${err.message}\n`);
  }
}

function handleRemove() {
  return prompt("Enter the title of the book to remove: ").then((title) => {
    console.log("\nRemove a Book\n");
    collection.removeBook(title);
    console.log("\nBook removed if it existed.\n");
  });
}

async function handleFind() {
  console.log("\nFind Books by Author\n");

  const author = await prompt("Author name: ");
  const books = collection.findByAuthor(author);

  showBooks(books);
}

async function handleRead() {
  // Parse: read "Book Title"
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.log("\nUsage: read \"Book Title\"\n");
    return;
  }
  // Support quoted or unquoted title
  let title = args.slice(1).join(" ");
  if ((title.startsWith('"') && title.endsWith('"')) || (title.startsWith("'") && title.endsWith("'"))) {
    title = title.slice(1, -1);
  }
  const success = collection.markAsRead(title);
  if (success) {
    console.log(`\nMarked as read: "${title}"\n`);
  } else {
    console.log(`\nBook not found: "${title}"\n`);
  }
}

async function handleMarkAsRead(title) {
  try {
    const result = collection.markAsRead(title);
    if (result) {
      console.log(`\nMarked '${title}' as read.\n`);
    } else {
      console.log(`\nError: Book titled '${title}' not found.\n`);
    }
  } catch (err) {
    console.log(`\nError: ${err.message}\n`);
  }
}

function showHelp() {
  console.log(`
Book Collection Helper

Commands:
  list     - Show all books
  add      - Add a new book
  remove   - Remove a book by title
  find     - Find books by author
  read     - Mark a book as read by title. Usage: read "Book Title" (quotes required if the title has spaces)
  help     - Show this help message
`);
}

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    showHelp();
    return;
  }

  const command = args[0].toLowerCase();

  switch (command) {
    case "list":
      handleList();
      break;
    case "add":
      await handleAdd();
      break;
    case "remove":
      await handleRemove();
      break;
    case "find":
      await handleFind();
      break;
    case "read":
      await handleRead();
      break;
    case "markread":
      if (args[1]) {
        await handleMarkAsRead(args[1]);
      } else {
        const title = await prompt("Enter the title of the book to mark as read: ");
        await handleMarkAsRead(title);
      }
      break;
    case "help":
      showHelp();
      break;
    default:
      console.log("Unknown command.\n");
      showHelp();
      break;
  }
}

main();
