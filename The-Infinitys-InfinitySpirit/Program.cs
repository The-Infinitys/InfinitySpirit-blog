// The Infinity's Infinity Style Static Site Generator
/*
home/runner/work/InfinitySpirit/InfinitySpirit/The-Infinitys-InfinitySpirit/Program.cs(69,9): error CS8801: Cannot use local variable or local function 'isDirectDrive' declared in a top-level statement in this context. [/home/runner/work/InfinitySpirit/InfinitySpirit/The-Infinitys-InfinitySpirit/The-Infinitys-InfinitySpirit.csproj]

The build failed. Fix the build errors and run again.
*/
using System;
using System.IO;
using System.Text.Json;

Console.WriteLine("-------Infinity Style Static Site Generator-------");
List<string> folderList = GetFolderNames(Environment.CurrentDirectory);
bool isReleaseMode;
isReleaseMode = folderList.Contains("The-Infinitys-InfinitySpirit");
if (isReleaseMode)
{
  Console.WriteLine("Found The-Infinitys-InfinitySpirit. It is release mode");
}
else
{
  Console.WriteLine("Not Found The-Infinitys-InfinitySpiirt. It is test mode");
}

List<string> GetFolderNames(string currentDirectory)
{
  List<string> folderNames = new List<string>();

  foreach (var directory in Directory.EnumerateDirectories(currentDirectory))
  {
    folderNames.Add(Path.GetFileName(directory));
  }

  return folderNames;
}
List<string> GetFileNames(string currentDirectory)
{
  List<string> folderNames = new List<string>();

  foreach (var directory in Directory.EnumerateDirectories(currentDirectory))
  {
    folderNames.Add(Path.GetFileName(directory));
  }

  return folderNames;

}
GetFileNames(Environment.CurrentDirectory);
InfinityStyle.ReadSettingData(isReleaseMode);
Console.WriteLine(InfinityStyle.ConvertMarkdownToHTML(@"
# Hello!
THIS IS TEST
## Hello!
THIS IS TEST
### Hello!
THIS IS TEST
#### Hello!
THIS IS TEST
##### Hello!
THIS IS TEST
###### Hello!
THIS IS TEST

"));

// クラス等の用意
public struct htmlTemp
{
  private htmlTemp(string head, string foot)
  {
    head = "";
    foot = "";
  }
}

public class SettingData
{
  public bool isAutoDate { get; set; }
  public int CustomDateYear { get; set; }
  public int CustomDateMonth { get; set; }
  public string? RepositoryName { get; set; }
  public int RepositoryYear { get; set; }
}
public static class ConvertSetting
{
  public static int convertYear;
  public static int convertMonth;
}

public static class InfinityStyle
{
  public static SettingData? settingData;
  public static void ReadSettingData(bool isRelease)
  {
    StreamReader settingJsonFile;
    if (isRelease)
    {
      settingJsonFile = new StreamReader("./The-Infinitys-InfinitySpirit/setting/setting.json");
    }
    else
    {
      settingJsonFile = new StreamReader("./setting/setting.json");
    }
    string settingJsonText = settingJsonFile.ReadToEnd();
    Console.WriteLine("Read setting.json:\n\"\"\"\n" + settingJsonText + "\n\"\"\"");
    settingData = JsonSerializer.Deserialize<SettingData>(
        settingJsonText
    );
    Console.WriteLine("--------------------");
    Console.WriteLine("Read Setting Data");
    Console.WriteLine("--------------------");
    Console.WriteLine("Repository Name: " + settingData?.RepositoryName);
    Console.WriteLine("Repository Year: " + settingData?.RepositoryYear);
    bool isAutoDate;
    if (settingData is not null)
    {
      isAutoDate = settingData.isAutoDate == true;
    }
    else
    {
      isAutoDate = true;
    }
    if (isAutoDate)
    {
      DateTime dt = DateTime.Now;
      ConvertSetting.convertYear = dt.Year;
      ConvertSetting.convertMonth = dt.Month;
    }
    else
    {
      if (settingData?.CustomDateMonth is not null && settingData?.CustomDateYear is not null)
      {
        ConvertSetting.convertYear = settingData.CustomDateYear;
        ConvertSetting.convertMonth = settingData.CustomDateMonth;
      }
      else
      {
        DateTime dt = DateTime.Now;
        ConvertSetting.convertYear = dt.Year;
        ConvertSetting.convertMonth = dt.Month;
      }
    }
    Console.WriteLine("CustomDate Info:");
    Console.WriteLine("Convert Year: " + ConvertSetting.convertYear.ToString());
    Console.WriteLine("Convert Month: " + ConvertSetting.convertMonth.ToString());
    Console.WriteLine("--------------------");
  }
  public static string ConvertMarkdownToHTML(string markdown)
  {
    string[] lines;
    string result = "";
    lines = markdown.Split("\n");
    for (int i = 0; i < lines.Length; i++)
    {
      bool converted = false;
      string line = lines[i];
      for (int j = 0; j < 6; ++j)
      {
        if (line.StartsWith(new String('#', j + 1) + " "))
        {
          Console.WriteLine(line);
          string innertext = line.Substring(j + 2);
          Console.WriteLine(innertext);
          result += "<h" + (j + 1).ToString() + ">";
          result += innertext;
          result += "</h" + (j + 1).ToString() + ">\n";
          j = 6;  // 強制終了
          converted = true;
        }
      }
      if (!converted)
      {
        result += line + "\n";
      }
    }
    return result;
  }
}
